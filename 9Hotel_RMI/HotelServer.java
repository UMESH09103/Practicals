// HotelServer.java

import java.rmi.Naming;

public class HotelServer {
    public static void main(String[] args) {
        try {
            HotelInterface obj = new HotelImpl();

            Naming.rebind("rmi://localhost/HotelService", obj);

            System.out.println("Hotel Server is running...");
        } catch (Exception e) {
            System.out.println("Server error: " + e);
        }
    }
}