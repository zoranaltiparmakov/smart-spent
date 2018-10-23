package si.smartspent.smartspent;

import android.content.Context;

/**
 * Class used for APIs and usful methods
 */
public class Utils {
    // Django backend for auth and data
    public static final String API_URL = "https://smartspent.si/api/";

    public static void setToken(Context context, String access_token) {
        context.getSharedPreferences(context.getString(R.string.app_name), Context.MODE_PRIVATE)
                .edit().putString("token", access_token).apply();
    }

    public static String getToken(Context context) {
        return context.getSharedPreferences(context.getString(R.string.app_name), Context.MODE_PRIVATE)
                .getString("token", "");
    }

    public static void removeToken(Context context, String access_token) {
        context.getSharedPreferences(context.getString(R.string.app_name), Context.MODE_PRIVATE)
                .edit().clear().apply();
    }

    public static Boolean isLoggedIn(Context context) {
        return getToken(context) != null ? true : false;
    }

    public static boolean isEmailValid(String email) {
        return email.contains("@");
    }

    public static boolean isPasswordValid(String password) {
        return password.length() > 6;
    }
}
