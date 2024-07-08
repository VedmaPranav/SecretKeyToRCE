import java.security.*;
import javax.crypto.spec.*;
import java.util.Base64;
import javax.crypto.*;

public class Encryptor {

    public static final String key = "StRonGEncRyPDeCR";

    public static void main(String[] args) {
        try {
            String data = null;
            if (Integer.parseInt(args[1]) == 1) {
                data = encrypt(args[0]);
            } else {
                data = decrypt(args[0]);
            }
            System.out.println("Data : " + data);

        } catch (Exception ignored) {
            System.out.println(ignored);
        }
    }

    public static String encode(byte[] data) {
        return Base64.getEncoder().encodeToString(data);
    }

    public static byte[] decode(String data) {
        return Base64.getDecoder().decode(data);
    }

    public static String decrypt(String encryptedData) throws Exception {
        byte[] dataInBytes = decode(encryptedData);
        Cipher decryptionCipher = getCipher(true);
        byte[] decryptedBytes = decryptionCipher.doFinal(dataInBytes);
        return new String(decryptedBytes);
    }

    public static String encrypt(String data) throws Exception {
        byte[] dataInBytes = data.getBytes();
        Cipher encryptionCipher = getCipher(false);
        byte[] encryptedBytes = encryptionCipher.doFinal(dataInBytes);
        return encode(encryptedBytes);
    }

    public static Cipher getCipher(boolean decryptMode)
            throws InvalidKeyException, NoSuchAlgorithmException, NoSuchPaddingException {
        Key aesKey = new SecretKeySpec(key.getBytes(), "AES");
        Cipher cipher = Cipher.getInstance("AES");
        if (decryptMode) {
            cipher.init(Cipher.DECRYPT_MODE, aesKey);
        } else {
            cipher.init(Cipher.ENCRYPT_MODE, aesKey);
        }
        return cipher;
    }
}
