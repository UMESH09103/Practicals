// StringConcatImpl.java

import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;

public class StringConcatImpl extends UnicastRemoteObject implements StringConcat {

    protected StringConcatImpl() throws RemoteException {
        super();
    }

    @Override
    public String concatenate(String str1, String str2) throws RemoteException {
        return str1 + str2;
    }
}