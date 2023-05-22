
tdd:
	git ls-files |  entr make check

check:
	doit
	cd /tmp/ ; ls test_pp_* ; cat test_pp_*/*/*.py ; rm -r test_pp_*
	echo "ok"
