from typing import Iterator, Collection, Optional

from . import reglib


def _pprint_result(result: reglib.SearchResult, prefix: str = ""):
    key, display_name, val_name, val, vals, search_str = result

    print(f"{prefix}{display_name}", end="")

    name_of_OS_path_data_entry_name = next(key.names_of_path_env_variables(), None)

    if name_of_OS_path_data_entry_name is not None:
        print(
            f", includes {name_of_OS_path_data_entry_name}: {vals[name_of_OS_path_data_entry_name]}"
        )
    elif val_name or val:
        print(f", for: {val_name=}, {val=}", end="")
    elif display_name:
        print(f", with: {vals=}")

    print(f" at: {key}")


def _matching_uninstallers(
    search_terms: Collection[str],
) -> Iterator[reglib.SearchResult]:
    for uninstaller_key in reglib.uninstallers_keys:
        yield from uninstaller_key.search_key_and_subkeys_for_text(
            search_terms,
            search_children_of_keys_containing_text=True,
        )


class MatchingUninstallersFound(Exception):
    pass


def check_uninstallers(search_terms: Collection[str]) -> None:
    found = []

    for result in _matching_uninstallers(search_terms):
        found.append(result)
        _pprint_result(prefix="Matching uninstaller: ", result=result)

    if found:
        raise MatchingUninstallersFound(
            "Matching uninstaller(s) found. Run these uninstallers first before purging. "
        )


global_root = reglib.GlobalRoot()


def search_registry_for_text(
    search_terms: Collection[str], max_depth: Optional[int] = 5
) -> Iterator[reglib.SearchResult]:
    yield from global_root.search_key_and_subkeys_for_text(
        search_terms, max_depth=max_depth
    )


def search_registry(
    search_terms: Collection[str],
    max_depth: Optional[int] = None,
) -> None:
    try:
        check_uninstallers(search_terms)
    except MatchingUninstallersFound as e:
        print(
            "\n################################################################################\n"
            f"# {e.args[0]} #\n"
            "################################################################################\n"
        )

    print(
        f"Searching for Registry keys containing: {search_terms}.\n"
        f'Rerun win_purge with "--purge-registry" to delete the following registry keys (confirmation for each required): '
    )

    for i, result in enumerate(search_registry_for_text(search_terms, max_depth)):
        key, __, __, __, __, __ = result  # type: ignore
        if key.contains_path_env_variable():
            _pprint_result(
                prefix=f"{i}) Match found in System Path registry key: ", result=result
            )
        else:
            _pprint_result(prefix=f"{i}) Matching registry key: ", result=result)

    return None


def _delete_values_or_keys_from_registry(
    search_terms: Collection[str],
    max_depth: Optional[int] = None,
) -> None:
    if "" in search_terms:
        raise ValueError(
            "Deleting the entire Windows registry is not a supported feature. \n"
            "Purging based on an empty string will purge all registry keys."
        )

    print("WARNING!! Deleting the following Registry keys: ")

    for i, result in enumerate(search_registry_for_text(search_terms, max_depth)):
        key, display_name, val_name, val, vals, search_str = result

        if key.restricted():
            _pprint_result(
                prefix=f"{i}) Cannot delete match found in restricted key: ",
                result=result,
            )
            continue

        if not key.in_alterable_root():
            _pprint_result(
                prefix=f"{i}) Cannot delete match found in sub key of restricted root: ",
                result=result,
            )
            continue

        names_of_path_env_variables = set(key.names_of_path_env_variables())

        if names_of_path_env_variables:
            _pprint_result(
                prefix=f"{i}) Match found in System Path registry key: ", result=result
            )

            confirmation = ""

            for path_val_name in names_of_path_env_variables:
                system_paths = set(vals[path_val_name].split(";"))
                matching_paths = {
                    path
                    for path in system_paths
                    if any(str_.lower() in path.lower() for str_ in search_terms)
                }
                confirmation = input(
                    f"Remove: {matching_paths} from registry key Path value? (y/n/quit) "
                )

                if confirmation.lower().startswith("q"):
                    return

                if confirmation.lower() == "y":
                    writeable_key = reglib.ReadAndWritableKey.from_key(key)
                    writeable_key.set_registry_value_data(
                        name=path_val_name,
                        data=";".join(system_paths - matching_paths),
                        type_=1,
                    )

        elif val_name or val:
            key_with_deletable_values = (
                reglib.KeyWithDeletableValueNamesAndValues.from_key(key)
            )
            vals_and_names = set(
                key_with_deletable_values.vals_or_val_names_containing(search_terms)
            )
            vals_and_names -= names_of_path_env_variables
            for val_name_i, val_i in vals_and_names:
                message = f"Remove value name/val: {val_name_i!r}/{val_i!r} from registry key: {key}? (y/n/quit/skip val name) "

                confirmation = input(message)

                if confirmation.lower().startswith("q"):
                    return
                elif confirmation.lower().startswith("s"):
                    break
                elif confirmation.lower().startswith("y"):
                    key_with_deletable_values.delete_value_and_value_name(val_name_i)

        if search_str:
            _pprint_result(prefix=f"{i}) Matching registry key: ", result=result)

            if not key.can_delete_subkeys_of_parents():
                print(f"{i} Cannot delete sub keys of some parent of: {key}")
                continue

            confirmation = input(f"Delete registry key: {key}? (y/n/quit) ")

            if confirmation.lower().startswith("q"):
                return

            if confirmation.lower() == "y":
                deletable_key = reglib.DeletableKey.from_key(key)
                deletable_key.delete()


def delete_values_or_keys_from_registry(search_terms: Collection[str]) -> None:
    check_uninstallers(search_terms)
    _delete_values_or_keys_from_registry(search_terms)
