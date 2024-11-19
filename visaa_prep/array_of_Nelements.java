import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int[] arr = new int[n];
        for (int i=0;i<n;i++){
            arr[i]=i+1;
        }
        for(int i=0;i<n;i++){
            System.out.println(arr[i]);
            if(i<n-1){
                System.out.print(" ");
            }
        }
