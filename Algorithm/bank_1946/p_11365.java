//!밀비 급일

package bank_1946;

import java.util.Scanner;

public class p_11365{
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        String code = sc.nextLine();
        while(code.equals("END")){
            for(int i=code.length()-1;i>=0;i--){
                System.out.print(code.charAt(i));
            }
            System.out.println();
            code = sc.nextLine();
        }
        sc.close();
	}
}