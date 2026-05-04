// Server.java

import java.rmi.Naming;
import java.rmi.registry.LocateRegistry;

public class Server {
    public static void main(String[] args) {
        try {
            // Start RMI registry
            LocateRegistry.createRegistry(1099);

            // Create object
            StringConcatImpl obj = new StringConcatImpl();

            // Bind object to name
            Naming.rebind("rmi://localhost/StringService", obj);

            System.out.println("Server is running...");

        } catch (Exception e) {
            System.out.println("Server error: " + e);
        }
    }
}