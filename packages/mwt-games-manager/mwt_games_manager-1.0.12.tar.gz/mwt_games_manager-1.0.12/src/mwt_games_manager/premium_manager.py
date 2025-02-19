from datetime import datetime
import mwt_games_manager.managers as mg
from mwt_games_manager.models.premium import Premium


def add_premium(premium, username, game_name=None):
    """
    adds a premium feature to the game data of the user
    :param premium:
    :param username:
    :param game_name:
    :return:
    """
    if not game_name:
        game_name = mg.default_game_name
    mg.client.collection("users").document(username).collection("game-data").document(game_name).collection(
        "premiums").document(premium.name).set(premium.__dict__)


def update_premium(premium, username, game_name=None):
    """
    updates the premium feature information for the user
    :param premium:
    :param username:
    :param game_name:
    :return:
    """
    if not game_name:
        game_name = mg.default_game_name
    mg.client.collection("users").document(username).collection("game-data").document(game_name).collection(
        "premiums").document(premium.name).set(premium.__dict__)


def delete_premium(premium_name, username, game_name=None):
    """
    deletes a premium feature from the users premiums
    :param premium_name:
    :param username:
    :param game_name:
    :return:
    """
    if not game_name:
        game_name = mg.default_game_name
    mg.client.collection("users").document(username).collection("game-data").document(game_name).collection(
        "premiums").document(premium_name).delete()


def get_premium(premium_name, username, game_name=None):
    """
    fetches the premium feature information
    :param premium_name:
    :param username:
    :param game_name:
    :return:
    """
    if not game_name:
        game_name = mg.default_game_name
    premium = mg.client.collection("users").document(username).collection("game-data").document(game_name).collection(
        "premiums").document(premium_name).get().to_dict()

    if premium is None:
        return False

    return Premium(**premium)


def has_premium(premium_name, username, game_name=None):
    """
    determines if the user has the specified premium or not
    :param premium_name:
    :param username:
    :param game_name:
    :return:
    """
    if not game_name:
        game_name = mg.default_game_name
    premium = mg.client.collection("users").document(username).collection("game-data").document(game_name).collection(
        "premiums").document(premium_name).get().to_dict()

    if premium is None:
        return False

    if premium.trial:
        return premium.trial_end >= datetime.now()

    return True
