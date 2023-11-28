package com.example.appviena;

import java.util.ArrayList;
import java.util.Date;
import com.example.appviena.ProductoComanda;

public class Comanda {
    private int id;
    private Date fecha;
    private double total;
    private ArrayList<ProductoComanda> productos; // Una lista de productos con sus cantidades

    public Comanda(int id, Date fecha, double total, ArrayList<ProductoComanda> productos) {
        this.id = id;
        this.fecha = fecha;
        this.total = total;
        this.productos = productos;
    }

    // Getters y Setters
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public Date getFecha() {
        return fecha;
    }

    public void setFecha(Date fecha) {
        this.fecha = fecha;
    }

    public double getTotal() {
        return total;
    }

    public void setTotal(double total) {
        this.total = total;
    }

    public ArrayList<ProductoComanda> getProductos() {
        return productos;
    }

    public void setProductos(ArrayList<ProductoComanda> productos) {
        this.productos = productos;
    }

    // Puedes añadir más métodos aquí, como un método para calcular el total de la comanda
}