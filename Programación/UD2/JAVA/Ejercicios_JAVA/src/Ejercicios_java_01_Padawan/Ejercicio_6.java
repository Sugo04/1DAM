/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Ejercicios_java_01_Padawan;

/**
 * Alumno: Héctor Martín Ortega
 * 1º GS Desarrollo de Aplicaciones Multiplataforma
 * 
 * *************************ENUNCIADO****************************************
 * Ejercicio_6: Escribe un programa que dado el precio de un artículo y 
 * el precio de venta real nos muestre el porcentaje de descuento realizado.
 * **************************************************************************
 */

//Importamos el java.util.Scanner
import java.util.Scanner;
public class Ejercicio_6 {
    
     public static void main(String[] args){
    
        //Especificamos las variables del ejercicio
        double precio_artículo, precio_venta, descuento;
        
        
        //Escribo los objetos lector y entrada los cuales on un scanner
        Scanner lector = new Scanner(System.in);
        Scanner entrada = new Scanner(System.in);
        
        /**
         * Ahora muestro en pantalla el mensaje que dirá que se introduzca el 
         * valor para el precio del artículo y el precio de venta.
         */
        
        System.out.println("Introduzca el precio del artículo y "
                + "posteriormente el precio ded venta: ");
        
        //utilizo lo siguiente para leer ambos precios
        precio_artículo = lector.nextDouble();
        precio_venta = entrada.nextDouble();
        
        /**
         * Calculamos el descuento aplicado en el artículo, usease,
         * 
         * (precioventa*100/precio del artículo)-100.
         */
        descuento = 100 -(precio_venta*100/precio_artículo);
         System.out.println(descuento+"%");
     }
    
}
