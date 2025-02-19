


class BaseDFSM:
    def __init__(self, master):
        self.master = master

    """##### Реализация функционала DFSM #####"""
    """
    Класс DFSM предназначен для хранения состояний отделенных потоков и вызова функции в соответствии с состоянием.
    Состояния отделенных потоков храняться в json формате: 
    {
        "class_name": {
                        "1234": {
                            "current_state": "test",
                            "previous_different_state": "last",
                            "previous_state": "test"
                      }
        }
    }
    ,где 
    class_name - Строка, которая определеяет в каком месте кода используется машина состояний, (На один класс может быть несколько машин состояний)
    "1234" - уникальный id отделенного потока, при вытягивании из json преобразуется в int формат
    "current_state" - текущее состояние пользователя
    "previous_different_state" - предыдущее отличающееся состояние
    "previous_state" - предыдущее состояние

    Для соверщения переходов (вызовов функций с параметрами) используется json_h (Правила использования соответствуют использованию json_h).
    Хранящийся конфигурационный файл имеет вид:
    {
        "class_name": {
            "state_1": {"function": "function.path","params": ["param_name_1","param_name_2"]}
        }
    }
    ,где
    class_name - Строка, которая определеяет в каком месте кода используется машина состояний, (На один класс может быть несколько машин состояний)
    state_1 - Строка, которая определяет состояние
    function.path - пример ссылки на функцию, которая идет после self без (), ссылка должна быть относительно текущего класса, может использовать вложенность self.function.path() 
    ["param_name_1","param_name_2"] - параметры, которые будут вытянуты из локальных переменных для передачи параметров в функцию перехода
    """


    """######## РАБОТА С БАЗОЙ ПОЛЬЗОВАТЕЛЬСКИХ СОСТОЯНИЙ #######"""
    def get_project_states_json(self):
        """ Вытянуть состояния из json """
        self.project_states = self.json_h.unload(self.db_sates, {})
        # Преобразование ключей на 2 уровне вложенности в число, если это "1234"
        self.project_states = {outer_key: {int(k) if isinstance(k, str) and k.isdigit() else k: v for k, v in inner_dict.items()} if isinstance(inner_dict, dict) else inner_dict for outer_key, inner_dict in self.project_states.items()}

    def set_project_states_json(self):
        """ Сохранить состояния в json """
        self.json_h.load(self.project_states, self.db_sates)

    def set_state(self, class_name, division_id, state):
        """ Установить состояние"""
        class_data = self.project_states.setdefault(class_name, {})
        user_data = class_data.setdefault(division_id, {})

        if "current_state" not in user_data:
            user_data["current_state"] = state
        else:
            if user_data["current_state"] != state or "previous_different_state" not in user_data:
                user_data["previous_different_state"] = user_data["current_state"]
            user_data["previous_state"] = user_data["current_state"]
            user_data["current_state"] = state
        self.set_project_states_json()

    def get_state(self, class_name, division_id, type_state):
        """ Вытянуть состояние """
        if class_name not in self.project_states:
            return None

        if division_id not in self.project_states[class_name]:
            return None

        division_data = self.project_states[class_name][division_id]

        if type_state in division_data:
            return division_data[type_state]
        else:
            return None

    """###### РАБОТА С КОНФИГУРАЦИЕЙ ПЕРЕХОДОВ #######"""

    def get_config_param(self, class_name, state, field):
        """ Вытянуть параметры из конфига """
        try:
            config = self.states_config.get(class_name)
            return config[state][field]
        except TypeError as e:
            if class_name == "master":
                raise TypeError(
                    'Перенесите базовую конфигурацию для master в DFSM_config.json\n\n\t"master": {\n\t\t"wait": {"function": "wait", "params": []},\n\t\t"stop": {"function": "stop", "params": []}\n\t}')
            else:
                raise TypeError(f"Вы неправильно заполнили конфигурационный файл DFSM_config.json: Ожидается {field} в поле {class_name}")
        except KeyError as e:
            if e.args[0] == "wait" and class_name == "master":
                raise TypeError(
                    'Перенесите базовую конфигурацию для master в DFSM_config.json\n\n\t"master": {\n\t\t"wait": {"function": "wait", "params": []},\n\t\t"stop": {"function": "stop", "params": []}\n\t}')
            else:
                raise

    """###### ПРЕОБРАЗОВАНИЕ ИМЕН В ССЫЛКИ ########"""

    def get_params(self, class_name, state, local_vars):
        """
            Вытягивание имен переменных из конфига, преобразование в ссилки на переменные локальной области видимости
            конфиг -> имена аргументов -> ссылки на переменные
        :param class_name, state: аргументы пути конфигурационного файла для распаковки имен
        :param local_vars: local() из требуемой функции
        """
        params_name = self.get_config_param(class_name, state, "params")
        args = tuple(local_vars[key] for key in params_name if key in local_vars)
        return args

    def get_function_by_path(self, _object, function_path):
        """
            Преобразование строки пути вида self.registration_handler.start_registration в ссылку на функцию
            имя функции -> ссылка функции
        :param _object: self объекта вызывателя - корень пути
        :param function_path: имя функции
        :return: ссылка на функцию
        """
        parts = function_path.split('.')
        function = _object
        for part in parts:
            function = getattr(function, part)
        return function

    """###### ОСНОВА ФУНКЦИОНАЛА. РЕАЛИЗАЦИЯ ПЕРЕХОДОВ ######"""
    def get_function_distributions(self, _object, class_name, state):
        """
            Вытянуть ссылку на фукнцию из конфига
            конфиг -> имя функции -> ссылка фунции
            Этапы:
                1. Вытянуть путь из конфигурационного файла
                2. Преобразвать имени пути в ссылку
        """
        function_path = self.get_config_param(class_name, state, "function")
        function = self.get_function_by_path(_object, function_path)
        return function

    def implement_transition(self, _object, class_name, state, local_vars):
        """
            Совершение перехода
            Этапы:
                1. Вытянуть необходимые параметры для функици
                2. Вытянуть путь функции
                3. Вызвать функцию
        """
        params = self.get_params(class_name, state, local_vars)

        transition_function = self.get_function_distributions(_object, class_name, state)

        transition_function(*params)


    def distributions_prompt(self, _object, class_name, division_id, local_vars):
        """
            Совершение полного стандартного перехода
        :param _object: ссылка self на обьект вызыватель
        :param class_name: имя класса вызывателя
        :param division_id: ид отделенного потока
        :param local_vars: locals() из вызывателя
        """
        state              = self.get_state(class_name, division_id, "current_state")
        if state:
            self.implement_transition(_object, class_name, state, local_vars)
        else:
            print(f"Поток не найден! division_id: {division_id}")


    async def async_distributions_prompt(self, _object, class_name, division_id, local_vars):
        """
                    Совершение полного стандартного перехода
                :param _object: ссылка self на обьект вызыватель
                :param class_name: имя класса вызывателя
                :param division_id: ид отделенного потока
                :param local_vars: locals() из вызывателя
                """
        state = self.get_state(class_name, division_id, "current_state")
        if state:
            await self.async_implement_transition(_object, class_name, state, local_vars)
        else:
            print(f"Поток не найден! division_id: {division_id}")

    async def async_implement_transition(self, _object, class_name, state, local_vars):
        """
            Совершение перехода
            Этапы:
                1. Вытянуть необходимые параметры для функици
                2. Вытянуть путь функции
                3. Вызвать функцию
        """
        params = self.get_params(class_name, state, local_vars)

        transition_function = self.get_function_distributions(_object, class_name, state)

        await transition_function(*params)
