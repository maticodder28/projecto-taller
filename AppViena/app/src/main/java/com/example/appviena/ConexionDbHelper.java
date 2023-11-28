package com.example.appviena;

import android.content.ContentValues;
import android.content.Context;
import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.SQLiteOpenHelper;
import androidx.annotation.Nullable;

public class ConexionDbHelper extends SQLiteOpenHelper {

    // Versión de la base de datos y nombre
    private static final int DATABASE_VERSION = 2;
    private static final String DATABASE_NAME = "appviena.db";

    // Nombres de las tablas
    public static final String TABLE_USERS = "usuarios";
    public static final String TABLE_PRODUCTS = "productos";
    public static final String TABLE_ORDERS = "comandas";
    public static final String TABLE_ORDER_DETAILS = "detalles_comanda";

    // Columnas comunes
    public static final String COLUMN_ID = "id";

    // Columnas de la tabla 'usuarios'
    public static final String COLUMN_NAME = "nombre";
    public static final String COLUMN_APELLIDO = "apellido";
    public static final String COLUMN_EMAIL = "email";
    public static final String COLUMN_CLAVE = "clave";
    public static final String COLUMN_IS_SUPERUSER = "is_superuser";

    // Columnas de la tabla 'productos'
    public static final String COLUMN_DESCRIPTION = "descripcion";
    public static final String COLUMN_PRICE = "precio";

    // Columnas de la tabla 'comandas'
    public static final String COLUMN_FECHA = "fecha";
    public static final String COLUMN_TOTAL = "total";
    public static final String COLUMN_USUARIO_ID = "usuario_id";

    // Columnas de la tabla 'detalles_comanda'
    public static final String COLUMN_COMANDA_ID = "comanda_id";
    public static final String COLUMN_PRODUCTO_ID = "producto_id";
    public static final String COLUMN_CANTIDAD = "cantidad";

    // SQL para crear tablas
    private static final String SQL_CREATE_USERS =
            "CREATE TABLE " + TABLE_USERS + " (" +
                    COLUMN_ID + " INTEGER PRIMARY KEY AUTOINCREMENT," +
                    COLUMN_NAME + " TEXT," +
                    COLUMN_APELLIDO + " TEXT," +
                    COLUMN_EMAIL + " TEXT," +
                    COLUMN_CLAVE + " TEXT," +
                    COLUMN_IS_SUPERUSER + " INTEGER DEFAULT 0" +
                    ")";

    private static final String SQL_CREATE_PRODUCTS =
            "CREATE TABLE " + TABLE_PRODUCTS + " (" +
                    COLUMN_ID + " INTEGER PRIMARY KEY AUTOINCREMENT," +
                    COLUMN_NAME + " TEXT," +
                    COLUMN_DESCRIPTION + " TEXT," +
                    COLUMN_PRICE + " REAL" +
                    ")";

    private static final String SQL_CREATE_ORDERS =
            "CREATE TABLE " + TABLE_ORDERS + " (" +
                    COLUMN_ID + " INTEGER PRIMARY KEY AUTOINCREMENT," +
                    COLUMN_USUARIO_ID + " INTEGER," +
                    COLUMN_FECHA + " TEXT," +
                    COLUMN_TOTAL + " REAL," +
                    "FOREIGN KEY(" + COLUMN_USUARIO_ID + ") REFERENCES " + TABLE_USERS + "(" + COLUMN_ID + ")" +
                    ")";

    private static final String SQL_CREATE_ORDER_DETAILS =
            "CREATE TABLE " + TABLE_ORDER_DETAILS + " (" +
                    COLUMN_COMANDA_ID + " INTEGER," +
                    COLUMN_PRODUCTO_ID + " INTEGER," +
                    COLUMN_CANTIDAD + " INTEGER," +
                    "FOREIGN KEY(" + COLUMN_COMANDA_ID + ") REFERENCES " + TABLE_ORDERS + "(" + COLUMN_ID + ")," +
                    "FOREIGN KEY(" + COLUMN_PRODUCTO_ID + ") REFERENCES " + TABLE_PRODUCTS + "(" + COLUMN_ID + ")" +
                    ")";

    public ConexionDbHelper(@Nullable Context context) {
        super(context, DATABASE_NAME, null, DATABASE_VERSION);
    }

    @Override
    public void onCreate(SQLiteDatabase db) {
        db.execSQL(SQL_CREATE_USERS);
        db.execSQL(SQL_CREATE_PRODUCTS);
        db.execSQL(SQL_CREATE_ORDERS);
        db.execSQL(SQL_CREATE_ORDER_DETAILS);
        insertSuperUser(db);
        insertInitialData(db);
    }
    private void insertSuperUser(SQLiteDatabase db) {
        ContentValues superUser = new ContentValues();
        superUser.put(COLUMN_NAME, "Matias");
        superUser.put("APELLIDO", "Munizaga");
        superUser.put("EMAIL", "MM@SUPERUSER.COM");
        superUser.put("CLAVE", "Ctm666!!"); // Recuerda usar una contraseña hasheada en una aplicación real
        superUser.put("is_superuser", 1);

        db.insert(TABLE_USERS, null, superUser);
    }
    private void insertInitialData(SQLiteDatabase db) {
        // Producto 1: Completo Italiano
        ContentValues valuesItaliano = new ContentValues();
        valuesItaliano.put(COLUMN_NAME, "Completo Italiano");
        valuesItaliano.put(COLUMN_PRICE, 1500);
        valuesItaliano.put(COLUMN_DESCRIPTION, "Pan, Vienesa, Tomate, Palta, Mayonesa Casera");
        db.insert(TABLE_PRODUCTS, null, valuesItaliano);

        // Producto 2: Coca Cola 350ml
        ContentValues valuesCocaCola = new ContentValues();
        valuesCocaCola.put(COLUMN_NAME, "Coca Cola 350ml");
        valuesCocaCola.put(COLUMN_PRICE, 1000);
        valuesCocaCola.put(COLUMN_DESCRIPTION, "Bebida de fantasía sabor cola");
        db.insert(TABLE_PRODUCTS, null, valuesCocaCola);
    }

    @Override
    public void onUpgrade(SQLiteDatabase db, int oldVersion, int newVersion) {
        db.execSQL("DROP TABLE IF EXISTS " + TABLE_USERS);
        db.execSQL("DROP TABLE IF EXISTS " + TABLE_PRODUCTS);
        db.execSQL("DROP TABLE IF EXISTS " + TABLE_ORDERS);
        db.execSQL("DROP TABLE IF EXISTS " + TABLE_ORDER_DETAILS);
        onCreate(db);
    }

    // Puedes agregar aquí cualquier otro método auxiliar necesario
}
