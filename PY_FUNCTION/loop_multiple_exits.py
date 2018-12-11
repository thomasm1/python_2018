"""thomas maestas
demonstrates a loop with multiple exits

#include <iostream> 
using namespace std;

int main(){
  string name;
  cout << "What is your name? ";
  cin >> name;
  cout << "Hello there, " << name << "!" << endl;
}
##
#include <stdio.h>
int main(){
  char userName[20];
  printf("What is your name? ");
  scanf("%s", userName);
  printf("Hi there, %s! \n", userName);
  return(0);
} // main
##
name = input("What is your name?")
print ("Hi, {}".format(name));
## 
//Hello.java
import java.util.*;

public class Hello {
  public static void main (String[] args){
    Scanner input = new Scanner(System.in);
    String userName;
    System.out.println("What is your name?");
    userName = input.nextLine();
    System.out.println("Hi there " + userName + "! ");
  } // end main
}
##
for i in range(start, finish, change):
  code
#
while (condition):
    changeCode
"""
correct = "hola!"
tries = 0

keepGoing = true
while(keepGoing):
  tries = tries + 1
  print ("try # ", tries)

  guess = input("What is the password? ")
  if guess = correct:
    print("That's right!")
    keepGoing = False
  
  elif tries >= 3:
    print("Too many wrong tries...")
    keepGoing = False