#!/usr/bin/python3
"""
--------------------------------------------------------------------------------
  @author         : Michaël Costa (michael.costa@mcos.nc)
  @date           : 04/02/2021
  @version        : 1.0.0
  @description    : Script de test

--------------------------------------------------------------------------------
  Mise a jour :
  1.0.0  04/02/2021 - Michaël Costa - Cre: Création

--------------------------------------------------------------------------------
  Liste des utilisateurs ou groupe autorisés:
    @user:root

--------------------------------------------------------------------------------
  Liste des paramètres de configuration obligatoires:
    <section>|<clef>|<type>|<secret>
    @conf:database|host|str
    @conf:database|port|int
    @conf:database|user|str|true
    @conf:database|password|str|true
    @conf:database|db|str
    @conf:git|host|str
    @conf:git|port|int
    @conf:git|user|str|true
    @conf:git|repo|str
    @conf:git|branch|str
    @conf:git|ssh_cmd|str
    @conf:smtp|host|str
    @conf:smtp|port|int
    @conf:pop|host|str
    @conf:pop|port|int
    @conf:pop|user|str|true
    @conf:pop|password|str|true
    @conf:ssh|host|str
    @conf:ssh|port|int
    @conf:ssh|user|str|true
    @conf:ssh|keyfile|str|true
    @conf:api|host|str
    @conf:api|port|int
    @conf:api|endpoint|str


--------------------------------------------------------------------------------
  Liste des paramètres des options et arguments d'exécution:
    <nom>|<type>|<help>|<num_args>|<defaut>|<conflit>|<implique>|<requis>|<secret>
    @args:remote_path|str|Chemin distant|1||||true|false
    @args:remote_filename|str|nom du fichier distant|1||||true|false
    @args:local_path|str|Chemin local|1||||true|false
    @args:mail_recipient|choice|Adresse de courriel du destinataire|1|harry.fink@flying.circus,luiggi,vercotti@flying.circus|||true|true


--------------------------------------------------------------------------------
  Fonctionnement:
  ---------------
    Script de test du cadriciel Scrippy.

    Ce script exploite un panel des fonctionnalités proposées par le cadriciel Scrippy telles que:
    - Exploitation d'API
    - Manipulation de base de données
    - Envoi (SMTP) et reception (POP3) de courriel
    - Exécution de commandes distantes (SSH)
    - Transfert de fichiers (SFTP)
    - Manipulation de dépôts Git
    - Manipulation de fichiers modèles (Template Jinja2)

  D'autres fonctionnalités sont disponibles: https://codeberg.org/scrippy
"""
# --------------------------------------------------------------------------
#  Initialisation de l’environnement
# --------------------------------------------------------------------------
import os
import json
import shutil
import scrippy_core
from scrippy_core import logger
from scrippy_db.db import Database
from scrippy_git.git import Repo
from scrippy_remote.ssh import Ssh
from scrippy_api.api.client import Client
from scrippy_template.template import Renderer
from scrippy_mail import ScrippyMailError
from scrippy_mail.pop import Client as PopClient
from scrippy_mail.smtp import Client as SmtpClient


# --------------------------------------------------------------------------
#  fonctions
# --------------------------------------------------------------------------
def get_api_user_list(host, port, endpoint):
  """Récupère la liste des utilisateurs à partir de l'API."""
  logger.info("[+] Récupération de la liste des utilisateurs depuis l'API")
  params = {}
  url = f"http://{host}:{port}/{endpoint}"
  client = Client(verify=False)
  response = client.request(method="GET", url=url, params=params)
  assert response.status_code == 200
  users = response.json()['users']
  for user in users:
    logger.info(f" '-> First name: {user['first_name']} / Last name: {user['last_name']} / Password: {user['password']}")
  return response.json()


def add_api_user(host, port, endpoint, user):
  """Ajoute un utilisateur à l'aide de l'API."""
  logger.info("[+] Ajout de l'utilisateur à l'aide de l'API")
  for attr in user["user"]:
    logger.info(f" '-> {attr}: {user['user'][attr]}")
  url = f"http://{host}:{port}/{endpoint}"
  client = Client(verify=False)
  response = client.request(method="PUT", url=url, data=json.dumps(user))
  assert response.status_code == 200
  return response.json()


def get_db_users(username, host, port, database, password):
  """Récupère la liste des utilisateurs à partir de la base de données."""
  logger.info("[+] Récupération de la liste des utilisateurs depuis la base de données")
  with Database(db_type="pgsql", username=username, host=host, port=port, database=database, password=password) as db:
    req = "select id, name, givenname, password from users order by id;"
    params = None
    users = db.query(query=req, params=params)
    for user in users:
      logger.info(f" '-> ID: {user[0]} / Last name: {user[1]} / First name: { user[2]} / Password: {user[3]}")
    return users


def add_db_user(username, host, port, database, password, user):
  """Ajout une utilisateur dans la base de données."""
  logger.info("[+] Ajout d'un utilisateur dans la base de données")
  for attr in user:
    logger.info(f" '-> {attr}")
  with Database(db_type="pgsql", username=username, host=host, port=port, database=database, password=password) as db:
    req = "insert into users values (DEFAULT, %s, %s, %s) returning id;"
    params = user
    result = db.query(query=req, params=params, commit=True)
    logger.info(result)
    return result


def render_template(template, params):
  """Rendu de fichiers modèles."""
  logger.info("[+] rendu du fichier modèle")
  logger.info(f" '-> {template}")
  base_path = scrippy_core.env.get("templatedir")
  renderer = Renderer(base_path, template)
  return renderer.render(params=params)


def send_mail(host, port, rcpt, body):
  """Envoi d'un courriel."""
  logger.info("[+] Envoi du courriel")
  with SmtpClient(host=host,
                  port=port,
                  ssl=False,
                  starttls=False) as smtp_client:
    sender = "luiggi.vercotti@flying.circus"
    recipients = [rcpt,]
    mail_subject = "Nobody expects the spanish inquisition"
    mail_body = body
    return smtp_client.send(subject=mail_subject,
                            body=mail_body,
                            sender=sender,
                            recipients=recipients)


def get_mail(host, port, username, password):
  """Récupération d'un courriel."""
  logger.info("[+] Récupération du courriel")
  with PopClient(host=host,
                 port=port,
                 username=username,
                 password=password,
                 ssl=False,
                 starttls=False) as pop_client:
    num_available_mails = pop_client.get_message_count()
    logger.info(f" '-> Nombre de courriels disponibles: {num_available_mails}")
    assert num_available_mails == 1
    logger.info("  '-> Ok")
    message = pop_client.get_message(number=1)
    logger.info(f" '-> {message}")
    return message


def delete_mail(host, port, username, password, num):
  """Suppression des courriels."""
  logger.info("[+] Suppression des courriels")
  with PopClient(host=host,
                 port=port,
                 username=username,
                 password=password,
                 ssl=False,
                 starttls=False) as pop_client:
    return pop_client.delete_message(number=num)


def git_clone(repo, branch, path, env):
  """Clonage de dépôt Git."""
  logger.info("[+] Clonage du dépôt:")
  repo.clone(branch=branch, path=path, env=env)


def git_push(repo, message):
  """Pousse les modifications vers le dépôt distant."""
  logger.info("[+] Envoi des modifications")
  repo.commit_push(message)


def ssh_exec_cmd(username, host, port, key, cmd):
  """Exécution d'une commande sur hôte distant."""
  logger.info("[+] Exécution de la commande sur l'hôte distant")
  logger.info(f" '-> {cmd}")
  with Ssh(username=username,
           host=host,
           port=port,
           key=key) as remote_host:
    return remote_host.exec(cmd, exit_on_error=True)


def ssh_send_files(username, host, port, key, local_path, local_filename, remote_path):
  """Envoi de fichiers sur hôte distant."""
  logger.info("[+] Envoi des fichiers via SSH")
  with Ssh(username=username,
           host=host,
           port=port,
           key=key) as remote_host:
    local_file = os.path.join(local_path, local_filename)
    remote_host.put_file(local_file=local_file,
                         remote_dir=remote_path,
                         exit_on_error=True)


def ssh_get_file(username, host, port, key, local_path, remote_path, remote_filename):
  """Récupération de fichier depuis l'hôte distant."""
  logger.info("[+] Récupération du fichier distant")
  with Ssh(username=username,
           host=host,
           port=port,
           key=key) as remote_host:
    remote_file = os.path.join(remote_path, remote_filename)
    remote_host.get_file(remote_file=remote_file,
                         local_dir=local_path,
                         create_dirs=False,
                         exit_on_error=True)
    remote_host.delete_remote_file(remote_file=remote_file,
                                   exit_on_error=True)


# --------------------------------------------------------------------------
#  Traitement principal
# --------------------------------------------------------------------------
def main():
  with scrippy_core.ScriptContext() as _context:
    config = _context.config
    args = _context.args
    logger.info("[+] Test started...")
    # --------------------------------------------------------------------------
    #  Test du client d'API
    # --------------------------------------------------------------------------
    new_user = {"user": {"first_name": "Harry", "last_name": "Fink", "password": "D3ADP4RR0T"}}
    expected = {"user": new_user["user"], "method": "PUT"}
    result = add_api_user(config.get("api", "host"), config.get("api", "port"), config.get("api", "endpoint"), new_user)
    assert result == expected
    result = get_api_user_list(config.get("api", "host"), config.get("api", "port"), config.get("api", "endpoint"))
    assert len(result["users"]) == 11
    assert new_user["user"] in result["users"]
    # --------------------------------------------------------------------------
    #  Test du client Base de données
    # --------------------------------------------------------------------------
    user = ("VERCOTTI", "Luiggi", "SP4N15H1NQU1S1T10N")
    result = add_db_user(config.get("database", "user"),
                         config.get("database", "host"),
                         config.get("database", "port", "int"),
                         config.get("database", "db"),
                         config.get("database", "password"),
                         user)
    assert result[0][0] == 1
    users = get_db_users(config.get("database", "user"),
                         config.get("database", "host"),
                         config.get("database", "port", "int"),
                         config.get("database", "db"),
                         config.get("database", "password"))
    assert len(users) == 2 and users[0][1] == "FINK" and users[0][2] == "Harry"
    assert users[1][0] == 1, users[1][1] == "VERCOTTI" and users[1][2] == "Luiggi"
    # --------------------------------------------------------------------------
    #  Test du moteur de modèles
    # --------------------------------------------------------------------------
    params = {"user": {"first_name": users[0][2],
                       "last_name": users[0][1],
                       "password": users[0][3]},
              "sender": {"first_name": users[1][2],
                         "last_name": users[1][1]}}
    mail_body = render_template(template=config.get("templates", "filename"), params=params)
    logger.info(mail_body)
    with open(os.path.join(scrippy_core.env.get("tmpdir"),
              "message.txt"),
              mode="w",
              encoding="utf-8") as message:
      message.write(mail_body)
    # --------------------------------------------------------------------------
    #  Test du client SMTP
    # --------------------------------------------------------------------------
    try:
      send_mail(host=config.get("smtp", "host"),
                port=config.get("smtp", "port", "int"),
                rcpt=args.mail_recipient,
                body=mail_body)
    except ScrippyMailError as err:
      logger.critical(str(err))
      raise err
    # --------------------------------------------------------------------------
    #  Test du client POP3
    # --------------------------------------------------------------------------
    mail_content = get_mail(host=config.get("pop", "host"),
                            port=config.get("pop", "port", "int"),
                            username=config.get("pop", "user"),
                            password=config.get("pop", "password"))
    assert mail_body.strip() in mail_content.strip()
    dele_result = delete_mail(host=config.get("pop", "host"),
                              port=config.get("pop", "port", "int"),
                              username=config.get("pop", "user"),
                              password=config.get("pop", "password"),
                              num=1)
    logger.info(dele_result)
    assert dele_result.decode()[:3] == "+OK"
    # --------------------------------------------------------------------------
    #  Test du client Git
    # --------------------------------------------------------------------------
    ssh_cmd = config.get("git", "ssh_cmd").format(os.path.dirname(os.path.realpath(__file__)))
    local_path = os.path.join(scrippy_core.env.get("tmpdir"),
                              config.get("git", "repo"))
    ENV = {"GIT_SSH_VARIANT": "ssh",
           "GIT_SSH_COMMAND": ssh_cmd}
    repo = Repo(username=config.get("git", "user"),
                host=config.get("git", "host"),
                port=config.get("git", "port", "int"),
                reponame=config.get("git", "repo"))
    git_clone(repo, branch=config.get("git", "branch"), path=local_path, env=ENV)
    shutil.copy(os.path.join(scrippy_core.env.get("tmpdir"),
                             "message.txt"),
                os.path.join(local_path, "message.txt"))
    git_push(repo, "Harry fink is a new user")
    # --------------------------------------------------------------------------
    #  Test du client SSH
    # --------------------------------------------------------------------------
    key = config.get("ssh", "keyfile").format(os.path.dirname(os.path.realpath(__file__)))
    ssh_send_files(username=config.get("ssh", "user"),
                   host=config.get("ssh", "host"),
                   port=config.get("ssh", "port", "int"),
                   key=key,
                   local_path=args.local_path,
                   local_filename=args.remote_filename,
                   remote_path=args.remote_path)
    cmd = f"find {args.remote_path} -type f"
    stdout = ssh_exec_cmd(username=config.get("ssh", "user"),
                          host=config.get("ssh", "host"),
                          port=config.get("ssh", "port", "int"),
                          key=key,
                          cmd=cmd)
    assert stdout["exit_code"] == 0
    ssh_get_file(username=config.get("ssh", "user"),
                 host=config.get("ssh", "host"),
                 port=config.get("ssh", "port", "int"),
                 key=key,
                 local_path=os.path.dirname(args.local_path),
                 remote_path=args.remote_path,
                 remote_filename=args.remote_filename)
    assert os.path.isfile(os.path.join(os.path.dirname(args.local_path), args.remote_filename))

    # --------------------------------------------------------------------------
    logger.info("[+] Test finished !")


# --------------------------------------------------------------------------
#  Point d'entrée
# --------------------------------------------------------------------------
if __name__ == '__main__':
  main()
