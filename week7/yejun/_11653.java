package week7.yejun;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class _11653 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        while (N > 1) {
            int i;
            for (i=2;;) {
                if (N == 1) return;

                if (N % i == 0) {
                    System.out.println(i);
                    N /= i;
                } else {
                    i++;
                }
            }
        }
    }
}
