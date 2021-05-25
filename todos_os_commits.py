from pydriller import Repository

for commit in Repository('C:\\Users\\Leandro César\\eclipse-workspace\\Analise_Git\\Junit4').traverse_commits():
    print(
        'The commit {} has been modified by {}, '
        'committed by {} in date {}'.format(
            commit.hash,
            commit.author.name,
            commit.committer.name,
            commit.committer_date
        )
    )