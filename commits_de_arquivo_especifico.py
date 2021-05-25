from pydriller import Repository

url = 'C:\\Users\\Leandro César\\eclipse-workspace\\Analise_Git\\Junit4'

for commit in Repository(url, filepath='C:\\Users\\Leandro César\\eclipse-workspace\\Analise_Git\\Junit4\\src\\test\\java\\junit\\samples\\AllTests.java').traverse_commits():
    print(commit.hash)
