public class Main {
    public static void main(String[] args) throws Exception {
        ProcessBuilder pb = new ProcessBuilder("python", "main.py");
        Process p = pb.start();
    }
}