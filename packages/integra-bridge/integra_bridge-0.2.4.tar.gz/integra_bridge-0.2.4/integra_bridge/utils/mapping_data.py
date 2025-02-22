async def parse_string_path(input_string: str) -> dict:
    target_path_config = {
        'root': None,
        'sequention': []
    }
    if input_string.startswith('#body'):
        target_path_config['root'] = 'body'

    input_string = input_string.replace('#body.', '')
    if not input_string == '':
        target_path_config['sequention'] = input_string.split('.')
    return target_path_config


async def get_root_object_by_path(
        body: dict | list,
        path: dict,
        default_object: dict | list | None = None,
        use_sequention: bool = True,
        *args,
        **kwargs
) -> dict | list:
    if path['root'] == 'body':
        root_object = body
    # elif path['root'] == 'context':
    # todo: current = context
    elif not path['root'] and default_object:
        root_object = default_object
    # По умолчанию если нет других данных используем корень тела сообщения
    elif not path['root'] and not default_object:
        root_object = body
    else:
        raise KeyError(f'Invalid path: Have to use tag or give a current object')

    if not path['sequention']:
        return root_object

    if use_sequention and isinstance(root_object, dict) and path['sequention']:
        for elem in path['sequention']:
            root_object = root_object.setdefault(elem, {})
    return root_object


async def set_by_sequention(meta: dict, path: list[str], value, return_only_target: bool = False,
                            default_filed_name: str = 'set_by_sequention') -> dict | list:
    """
    Устанавливает значение value в словаре data по списку ключей path.
    Если каких-то ключей по пути нет, они будут созданы.
    Возвращает исходный словарь data (изменённый).
    """
    if not path:
        meta[default_filed_name] = value
        return meta
    current = meta
    for key in path[:-1]:
        current = current.setdefault(key, {})
    current[path[-1]] = value
    return current[path[-1]] if return_only_target else meta
