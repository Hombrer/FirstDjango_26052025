### Расширенная инструкция по развертыванию проекта

1. Скачать  и установить: VirtualBox + Runtu_2404.ova
2. `sudo apt update`
3. `sudo apt install git python3.12-venv`
4. - `git config --global user.name "Name"`
5. - `git config --global user.email "mail@mail.com"`
6. `ssh-keygen`
7. - `cat ~/.ssh/id_ed25519.pub`
8. Добавить ssh ключ на сайт github.com
9. `mkdir Projects`
10. `cd Projects`
11. `git clone git@github.com:NameAccount/RepositoryName.git FirstDjango`
12. `cd FirstDjango`
13. Смотрим в `README.md` и выполняем инструкцию.
14. Внесли изменения и отправили на сервер:
15. - `git add .`
16. - `git commit -m "Message"`
17. - `git push` 