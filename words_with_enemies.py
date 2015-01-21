"""
Taken from http://www.reddit.com/r/dailyprogrammer/comments/2syz7y/20150119_challenge_198_easy_words_with_enemies/

Written by Jared Langenauer
1/21/2015
"""

def main():
	words = str(raw_input("Enter two words: "))
	word_list = words.split()
	left_string = word_list[0]
	right_string = word_list[1]
	
	new_lstr = left_string
	new_rstr = right_string
	for char in left_string:
		left_string = new_lstr
		right_string = new_rstr
		if char in right_string:
			# Get the first occurrence the char
			l_index = left_string.find(char)
			r_index = right_string.find(char)
			
			# Remove the char from each string 
			new_lstr = left_string[:l_index] + left_string[l_index+1:]
			new_rstr = right_string[:r_index] + right_string[r_index+1:]
			
	# Get final string lengths to determine winner
	left_size = len(new_lstr)
	right_size = len(new_rstr)
	
	if left_size > right_size:
		print "Left wins with " + str(left_size) + " letters left!"
	elif right_size > left_size:
		print "Right wins with " + str(right_size) + " letters left!"
	else:
		print "It's a tie!"
		
	print new_lstr, new_rstr
	
main()
