PROGRAMS = {

    "prime": {
        "Java": """
public class PrimeNumber {
    public static void main(String[] args) {
        int n = 17;
        boolean prime = true;

        for(int i=2;i<=n/2;i++) {
            if(n%i==0) {
                prime = false;
                break;
            }
        }

        System.out.println(prime ? "Prime" : "Not Prime");
    }
}
""",

        "Python": """
n = 17
prime = True

for i in range(2, n//2 + 1):
    if n % i == 0:
        prime = False
        break

print("Prime" if prime else "Not Prime")
""",

        "JavaScript": """
let n = 17;
let prime = true;

for(let i=2;i<=n/2;i++){
    if(n%i===0){
        prime = false;
        break;
    }
}

console.log(prime ? "Prime" : "Not Prime");
"""
    },

    "factorial": {
        "Java": """
public class Factorial {
    public static void main(String[] args) {
        int n = 5, fact = 1;

        for(int i=1;i<=n;i++) {
            fact *= i;
        }

        System.out.println(fact);
    }
}
""",

        "Python": """
n = 5
fact = 1

for i in range(1, n+1):
    fact *= i

print(fact)
""",

        "JavaScript": """
let n = 5;
let fact = 1;

for(let i=1;i<=n;i++){
    fact *= i;
}

console.log(fact);
"""
    },

    "palindrome": {
        "Java": """
public class Palindrome {
    public static void main(String[] args) {
        int num = 121, rev = 0, temp = num;

        while(temp > 0){
            rev = rev * 10 + temp % 10;
            temp /= 10;
        }

        System.out.println(num == rev ? "Palindrome" : "Not Palindrome");
    }
}
""",

        "Python": """
num = 121
rev = int(str(num)[::-1])

print("Palindrome" if num == rev else "Not Palindrome")
""",

        "JavaScript": """
let num = 121;

let rev = Number(
    String(num)
    .split('')
    .reverse()
    .join('')
);

console.log(num === rev ? "Palindrome" : "Not Palindrome");
"""
    },

    "fibonacci": {
        "Java": """
public class Fibonacci {
    public static void main(String[] args) {
        int a = 0, b = 1;

        for(int i=0;i<10;i++){
            System.out.print(a + " ");

            int c = a + b;
            a = b;
            b = c;
        }
    }
}
""",

        "Python": """
a, b = 0, 1

for i in range(10):
    print(a, end=" ")
    a, b = b, a + b
""",

        "JavaScript": """
let a = 0;
let b = 1;

for(let i=0;i<10;i++){
    console.log(a);

    let c = a + b;
    a = b;
    b = c;
}
"""
    },

    "armstrong": {
        "Java": """
public class Armstrong {
    public static void main(String[] args) {

        int num = 153;
        int temp = num;
        int sum = 0;

        while(temp > 0){
            int digit = temp % 10;

            sum += digit * digit * digit;

            temp /= 10;
        }

        System.out.println(
            sum == num ?
            "Armstrong" :
            "Not Armstrong"
        );
    }
}
""",

        "Python": """
num = 153
temp = num
sum = 0

while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10

print("Armstrong" if sum == num else "Not Armstrong")
""",

        "JavaScript": """
let num = 153;
let temp = num;
let sum = 0;

while(temp > 0){

    let digit = temp % 10;

    sum += digit * digit * digit;

    temp = Math.floor(temp / 10);
}

console.log(
    sum === num ?
    "Armstrong" :
    "Not Armstrong"
);
"""
    },
    "even odd": {
    "Java": """
public class EvenOdd {
    public static void main(String[] args) {
        int n = 10;
        System.out.println(n % 2 == 0 ? "Even" : "Odd");
    }
}
""",
    "Python": """
n = 10
print("Even" if n % 2 == 0 else "Odd")
""",
    "JavaScript": """
let n = 10;
console.log(n % 2 === 0 ? "Even" : "Odd");
"""
},

"leap year": {
    "Java": """
public class LeapYear {
    public static void main(String[] args) {
        int year = 2024;
        if((year%4==0 && year%100!=0) || year%400==0)
            System.out.println("Leap Year");
        else
            System.out.println("Not Leap Year");
    }
}
""",
    "Python": """
year = 2024
if (year%4==0 and year%100!=0) or year%400==0:
    print("Leap Year")
else:
    print("Not Leap Year")
""",
    "JavaScript": """
let year = 2024;
if((year%4===0 && year%100!==0) || year%400===0)
    console.log("Leap Year");
else
    console.log("Not Leap Year");
"""
},

"reverse string": {
    "Java": """
public class ReverseString {
    public static void main(String[] args) {
        String str = "Hello";
        String rev = new StringBuilder(str).reverse().toString();
        System.out.println(rev);
    }
}
""",
    "Python": """
s = "Hello"
print(s[::-1])
""",
    "JavaScript": """
let str = "Hello";
console.log(str.split('').reverse().join(''));
"""
},

"anagram": {
    "Java": """
import java.util.Arrays;
public class Anagram {
    public static void main(String[] args) {
        String s1="listen", s2="silent";
        char[] a=s1.toCharArray();
        char[] b=s2.toCharArray();
        Arrays.sort(a);
        Arrays.sort(b);
        System.out.println(Arrays.equals(a,b));
    }
}
""",
    "Python": """
s1="listen"
s2="silent"
print(sorted(s1)==sorted(s2))
""",
    "JavaScript": """
let s1="listen";
let s2="silent";
console.log(
s1.split('').sort().join('')===
s2.split('').sort().join('')
);
"""
},

"bubble sort": {
    "Java": """
public class BubbleSort {
    public static void main(String[] args) {
        int[] arr={5,3,8,1};

        for(int i=0;i<arr.length-1;i++){
            for(int j=0;j<arr.length-i-1;j++){
                if(arr[j]>arr[j+1]){
                    int temp=arr[j];
                    arr[j]=arr[j+1];
                    arr[j+1]=temp;
                }
            }
        }

        for(int n:arr)
            System.out.print(n+" ");
    }
}
""",
    "Python": """
arr=[5,3,8,1]

for i in range(len(arr)):
    for j in range(len(arr)-i-1):
        if arr[j] > arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]

print(arr)
""",
    "JavaScript": """
let arr=[5,3,8,1];

for(let i=0;i<arr.length;i++){
    for(let j=0;j<arr.length-i-1;j++){
        if(arr[j]>arr[j+1]){
            [arr[j],arr[j+1]]=[arr[j+1],arr[j]];
        }
    }
}

console.log(arr);
"""
},

"selection sort": {
    "Java": """
public class SelectionSort {
    public static void main(String[] args) {
        int[] arr = {64, 25, 12, 22, 11};

        for(int i=0;i<arr.length-1;i++) {
            int min = i;

            for(int j=i+1;j<arr.length;j++) {
                if(arr[j] < arr[min]) {
                    min = j;
                }
            }

            int temp = arr[min];
            arr[min] = arr[i];
            arr[i] = temp;
        }

        for(int n : arr)
            System.out.print(n + " ");
    }
}
""",

    "Python": """
arr = [64, 25, 12, 22, 11]

for i in range(len(arr)):
    min_idx = i

    for j in range(i+1, len(arr)):
        if arr[j] < arr[min_idx]:
            min_idx = j

    arr[i], arr[min_idx] = arr[min_idx], arr[i]

print(arr)
""",

    "JavaScript": """
let arr = [64,25,12,22,11];

for(let i=0;i<arr.length-1;i++){
    let min=i;

    for(let j=i+1;j<arr.length;j++){
        if(arr[j] < arr[min]){
            min=j;
        }
    }

    [arr[i],arr[min]]=[arr[min],arr[i]];
}

console.log(arr);
"""
},

"binary search": {
    "Java": """
public class BinarySearch {
    public static void main(String[] args) {

        int[] arr = {10,20,30,40,50};
        int target = 30;

        int left = 0;
        int right = arr.length - 1;

        while(left <= right){

            int mid = (left + right) / 2;

            if(arr[mid] == target){
                System.out.println("Found at index " + mid);
                return;
            }

            if(arr[mid] < target)
                left = mid + 1;
            else
                right = mid - 1;
        }

        System.out.println("Not Found");
    }
}
""",

    "Python": """
arr = [10,20,30,40,50]
target = 30

left = 0
right = len(arr)-1

while left <= right:

    mid = (left + right)//2

    if arr[mid] == target:
        print("Found at index", mid)
        break

    elif arr[mid] < target:
        left = mid + 1

    else:
        right = mid - 1
else:
    print("Not Found")
""",

    "JavaScript": """
let arr=[10,20,30,40,50];
let target=30;

let left=0;
let right=arr.length-1;

while(left<=right){

    let mid=Math.floor((left+right)/2);

    if(arr[mid]===target){
        console.log("Found at index " + mid);
        break;
    }

    if(arr[mid] < target)
        left=mid+1;
    else
        right=mid-1;
}
"""
},

"linear search": {
    "Java": """
public class LinearSearch {
    public static void main(String[] args) {

        int[] arr = {10,20,30,40,50};
        int target = 40;

        for(int i=0;i<arr.length;i++){

            if(arr[i] == target){
                System.out.println("Found at index " + i);
                return;
            }
        }

        System.out.println("Not Found");
    }
}
""",

    "Python": """
arr = [10,20,30,40,50]
target = 40

for i in range(len(arr)):

    if arr[i] == target:
        print("Found at index", i)
        break
else:
    print("Not Found")
""",

    "JavaScript": """
let arr=[10,20,30,40,50];
let target=40;

let found=false;

for(let i=0;i<arr.length;i++){

    if(arr[i]===target){
        console.log("Found at index " + i);
        found=true;
        break;
    }
}

if(!found)
    console.log("Not Found");
"""
},
"largest": {
    "Java": """
public class Largest {
    public static void main(String[] args) {
        int[] arr={10,20,5,40};
        int max=arr[0];

        for(int n:arr){
            if(n>max)
                max=n;
        }

        System.out.println(max);
    }
}
""",
    "Python": """
arr=[10,20,5,40]
print(max(arr))
""",
    "JavaScript": """
let arr=[10,20,5,40];
console.log(Math.max(...arr));
"""
},

"gcd": {
    "Java": """
public class GCD {
    public static void main(String[] args) {
        int a=12,b=18;

        while(b!=0){
            int t=b;
            b=a%b;
            a=t;
        }

        System.out.println(a);
    }
}
""",
    "Python": """
a,b=12,18

while b:
    a,b=b,a%b

print(a)
""",
    "JavaScript": """
let a=12,b=18;

while(b!==0){
    let t=b;
    b=a%b;
    a=t;
}

console.log(a);
"""
}

}