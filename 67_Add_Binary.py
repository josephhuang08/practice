class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ''' First solution
        out = []
        a = a[::-1]
        b = b[::-1]
        x = min(len(a), len(b))
        carry = 0
        for i in range(x):
            sum = int(a[i]) ^ int(b[i]) ^ carry
            if int(a[i]) + int(b[i]) + carry >= 2:
                carry = 1
            else:
                carry = 0
            out.append(sum)
        
        if len(a) > len(b):
            for i in range(x, len(a)):  
                sum = int(a[i]) ^ carry
                if int(a[i]) + carry >= 2:
                    carry = 1
                else:
                    carry = 0
                out.append(sum)

        elif len(b) > len(a):
            for i in range(x, len(b)):  
                sum = int(b[i]) ^ carry
                if int(b[i]) + carry >= 2:
                    carry = 1
                else:
                    carry = 0
                out.append(sum)

        if carry == 1:
            out.append(carry)
        out = out[::-1]
        ans = ''.join(str(e) for e in out)
        return ans
        '''
        # better code
        out = ""
        i, j, carry = len(a) - 1, len(b) - 1, 0
        while i >= 0 or j >= 0:
            sum = carry
            if i >= 0:
                sum += int(a[i])
            if j >= 0:
                sum += int(b[j])
            
            if sum >=2:
                carry = 1
                sum -= 2
            else:
                carry = 0

            out += str(sum)

            i, j = i - 1, j - 1
        
        if carry != 0:
            out += str(carry)
        
        return out[::-1]

s = Solution()
out = s.addBinary('11', '1')
print(out)
                
        
        
        
        
