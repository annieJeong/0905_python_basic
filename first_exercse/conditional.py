"""
if문 테스트
주어진 성적이 60점 이상일경우 패스
나머지 불합격
"""
def check_score(score):
    if score >= 60:
        return 'pass'
    else:
        return 'fail'

print(check_score(66))

