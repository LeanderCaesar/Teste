from pydriller import Repository

rm = Repository("https://github.com/avandeursen/dmm-test-repo")
for commit in rm.traverse_commits():
	print("| {} | {} | {} | {} | {} |".format(
	commit.msg,
	commit.dmm_unit_size,
	commit.dmm_unit_complexity,
	commit.dmm_unit_interfacing,
	commit.parents
	))




rm = Repository('https://github.com/avandeursen/dmm-test-repo', single='d7d62972125b33cf6e4ffdcccab5e7aac1014d62').traverse_commits()
