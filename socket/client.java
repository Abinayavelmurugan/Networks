import java.io.*;
import java.net.*;

public class client {
    public static void main(String[] args) {
        try {
            // Connect to the server on localhost and port 8080
            Socket socket = new Socket("localhost", 8080);

            // Setup streams to communicate with the server
            BufferedReader input = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            PrintWriter output = new PrintWriter(socket.getOutputStream(), true);

            // Send a message to the server
            output.println("Hello from client!");

            // Receive and print the server's response
            String serverMessage = input.readLine();
            System.out.println("Server says: " + serverMessage);

            // Close resources
            input.close();
            output.close();
            socket.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
