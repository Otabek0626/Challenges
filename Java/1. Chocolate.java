import java.util.Scanner;

class Chocolate{
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);

        System.out.print("How many raws of chocolate? ... ");
        int raw = input.nextInt();
        System.out.print("How many colums of chocolate? ... ");
        int colum = input.nextInt();
        System.out.print("How many piece you want to devide? ... ");
        int k = input.nextInt();

        float x = (float)raw / k;
        float y = (float)colum / k;
        if (x == raw/k || y == colum/k){
            System.out.println("Possible to devide");
        } else{
            System.out.println("impossible to devide");
        }
    }
}
