import java.io.*;
import java.net.*;

public class server {
    public static void main(String[] args) {
        try {
            // Create a server socket to listen on port 8080
            ServerSocket serverSocket = new ServerSocket(8080);
            System.out.println("Server is waiting for client on port 8080...");

            // Accept an incoming client connection
            Socket clientSocket = serverSocket.accept();
            System.out.println("Client connected!");

            // Setup streams to read from and write to the client
            BufferedReader input = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
            PrintWriter output = new PrintWriter(clientSocket.getOutputStream(), true);

            // Read and respond to client message
            String clientMessage = input.readLine();
            System.out.println("Client says: " + clientMessage);
            output.println("Hello from server!");

            // Close resources
            input.close();
            output.close();
            clientSocket.close();
            serverSocket.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
