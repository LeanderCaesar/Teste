from pydriller import Repository

for commit in Repository('https://github.com/williamsartijose/Trabalho-Cadastro-de-Aluno.git').traverse_commits():
    print(commit.hash)
    print(commit.msg)
    print(commit.author.name)
    print("\n")

    for file in commit.modified_files:
        print(file.filename, ' has changed')
    print("\n\n")