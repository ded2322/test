import subprocess

def commit(file_path, commit_message:str = "init"):
    try:
        subprocess.run(["git", "add", file_path],check=True)
        subprocess.run(["git", "commit", "-m", commit_message], check=True)
        print(f"Файл {file_path} успешно закоммичен с сообщением: {commit_message}")
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при выполнении команды Git: {e}")


def file():
    with open("test.txt", "a+") as f:
        f.write("new txt")

    commit(file_path="C:\\Users\\mdebc_nwrashl\\PycharmProjects\\githubs\\test.txt")

for _ in range(0,4):
    file()


