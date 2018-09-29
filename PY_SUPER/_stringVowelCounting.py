# This is my vowel counting code:
prophecy = "And there shall in that time be rumours of things going astray, and there will be a great confusion as to where things really are, and nobody will really know where lieth those little things with the sort of raffia work base, that has an attachment…at this time, a friend shall lose his friends’s hammer and the young shall not know where lieth the things possessed by their fathers that their fathers put there only just the night before around eight o’clock…"

vowel_count = 0
vowel_count += prophecy.count('a')
vowel_count += prophecy.count('A')
vowel_count += prophecy.count('e')
vowel_count += prophecy.count('E')
vowel_count += prophecy.count('i')
vowel_count += prophecy.count('I')
vowel_count += prophecy.count('o')
vowel_count += prophecy.count('O')
vowel_count += prophecy.count('u')
vowel_count += prophecy.count('U')
'''
Looking at this first attempt, I think I can make it better. Counting 
both lower-case 'a' and upper-case 'A', seems unnecessary. I'll convert 
everything to lower-case, and then I only need to count each vowel once!
'''

vowel_count = 0
lower_prophecy = prophecy.lower()
vowel_count += lower_prophecy.count('a')
vowel_count += lower_prophecy.count('e')
vowel_count += lower_prophecy.count('i')
vowel_count += lower_prophecy.count('o')
vowel_count += lower_prophecy.count('u')
print(vowel_count)
