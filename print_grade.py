def print_grade(sub1, score1, sub2, score2, sub3, score3):
	subs = [sub1, sub2, sub3]
	stars = []
	score = [score1, score2, score3]
	nums = [round(score1/5), round(score2/5), round(score3/5)]
	
	for i in range(3):
		stars.append("*" * nums[i])

	for i in range(3):
		print("{sub} : {star} ({score}점)".format(sub=subs[i], star=stars[i], score=score[i]))
