// HotelImpl.java

import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;
import java.util.HashMap;

public class HotelImpl extends UnicastRemoteObject implements HotelInterface {

    private HashMap<String, Integer> bookings;
    private int roomCounter;

    protected HotelImpl() throws RemoteException {
        bookings = new HashMap<>();
        roomCounter = 1;
    }

    public synchronized String bookRoom(String guestName) throws RemoteException {
        if (bookings.containsKey(guestName)) {
            return "Guest already has a booking!";
        }

        bookings.put(guestName, roomCounter);
        return "Room booked for " + guestName + " | Room No: " + (roomCounter++);
    }

    public synchronized String cancelBooking(String guestName) throws RemoteException {
        if (!bookings.containsKey(guestName)) {
            return "No booking found for " + guestName;
        }

        int room = bookings.remove(guestName);
        return "Booking cancelled for " + guestName + " | Room No: " + room;
    }
}