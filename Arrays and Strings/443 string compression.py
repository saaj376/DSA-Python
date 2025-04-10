class Solution:
    def compress(self, chars):
        write = 0
        read = 0
        while read < len(chars):
            char = chars[read]
            count = 0
            while read < len(chars) and chars[read] == char:
                read += 1
                count += 1
            chars[write] = char
            write += 1
            if count > 1:
                for c in str(count):
                    chars[write] = c
                    write += 1
        return write
    
#the time complexity is O(n) where n is the length of input list and we're only iterating over it once so overall time complexity is linear.
#the space complexity is O(1) because no extra space is allocated and only few integer variables are used.