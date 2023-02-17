package week6.yejun;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class _6588 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        // 소수 배열 구성
        int max = 1000000;
        int[] primes = new int[max+1];
        for (int i=2; i<=max; i++) primes[i] = i;

        for (int i=2; i<=max; i++) {
            if (primes[i] == 0) continue;

            for (int j=2*i; j<=max; j+=i) {
                primes[j] = 0;
            }
        }

        int n = Integer.parseInt(br.readLine());
        while (n != 0) {

            int a = 0;
            int b = 0;
            for (int i=3; i<n; i++) {
                if (i % 2 != 0 && primes[i] != 0) {
                    a = i;
                    if (n-a % 2 != 0 && primes[n-a] != 0 && n-a > a) {
                        b = n - a;
                        break;
                    }
                }
            }
            if (b == 0 || a == b) sb.append("Goldbach's conjecture is wrong.").append("\n");
            else sb.append(n + " = " + a + " + " + b).append("\n");

            n = Integer.parseInt(br.readLine());

        }

        System.out.println(sb);
    }
}
