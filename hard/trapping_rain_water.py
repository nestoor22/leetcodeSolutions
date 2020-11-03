class Solution:
    def trap(self, height) -> int:
        rain = 0
        left_pointer = 0
        rigth_pointer = len(height) - 1

        max_left = max_right = 0

        while left_pointer < rigth_pointer:
            if height[left_pointer] < height[rigth_pointer]:
                if height[left_pointer] > max_left:
                    max_left = height[left_pointer]
                else:
                    rain += max_left - height[left_pointer]

                left_pointer += 1
            else:
                if height[rigth_pointer] > max_right:
                    max_right = height[rigth_pointer]
                else:
                    rain += max_right - height[rigth_pointer]

                rigth_pointer -= 1

        return rain
