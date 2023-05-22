
tdd:
	git ls-files |  entr make check

check:
	doit
	cd /tmp/ ; ls test_pp_* ; rm -r test_pp_*
	echo "ok"
