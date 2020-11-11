

import java.util.Scanner;

public class Main extends oops {
	
	Scanner answer = new Scanner(System.in);
    
    int answer1 = answer.nextInt();
    public static void main(String[] args){
        Scanner answer = new Scanner(System.in);
        System.out.print("Select the numbers from 1 to 5... ");
        int answer1 = answer.nextInt();
        switch (answer1) {
            case 1:
                System.out.println(first());
                break;
            case 2:
                System.out.println(second());
                break;
            case 3:
                System.out.println(third());
                break;
            case 4:
                System.out.println(fourth());
                break;
            case 5:
                System.out.println(fifth());
                break;
        }
    }

}
