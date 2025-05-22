public class ReverseHello {
    public static void main(String[] args) {
        String s = "Hello, World!";
        System.out.println(new StringBuilder(s).reverse().toString());
    }
}
