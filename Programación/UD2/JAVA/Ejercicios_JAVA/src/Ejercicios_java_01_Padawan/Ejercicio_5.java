/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Ejercicios_java_01_Padawan;

/**
 * Alumno: Héctor Martín Ortega
 * 1º GS Desarrollo de Aplicaciones Multiplataforma
 * 
 * *************************ENUNCIADO*************************************
 * Ejercicio_5:Escribe un programa que toma como dato de entrada un número 
 * que corresponde a la longitud de un radio y nos escribe la longitud 
 * de la circunferencia el área del círculo y el volumen de la
 * esfera que corresponden con dicho radio.
 * ************************************************************************
 */

//Importamos el java.util.Scanner
import java.util.Scanner;

public class Ejercicio_5 {
    
    public static void main(String[] args){
    
        //Especificamos las variables del ejercicio
        double radio, longitud, área, volúmen;
        
        //Declaro el objeto lector el cual es un scanner
        Scanner lector = new Scanner(System.in);
        
        /**
         * Ahora muestro en pantalla el mensaje que dirá que se introduzca el 
         * valor para el radio.
         */
        
        System.out.println("Introduzca el radio requerido: ");
        
        //Introducimos el aparatado de entrada del radio
        radio = lector.nextDouble();
        
        //Ahora realizamos las operaciones necesarias
        
        longitud = (2*radio);
        /**
         * Necesitaremos pi para el área y el volumen, así que lo agregaremos 
         * con Math.PI .
         */
        área= (Math.PI*Math.pow(radio, 2)) ;
        volúmen=((4/3)*Math.PI*Math.pow(radio, 3));
        
        /**
         * Muestro en pantalla los resultado de las operaciones previamente 
         * resueltas.
        */
        
        System.out.println("El diámetro (longitud) de la circunferencia de"
                + " radio  "+radio+" es:"+longitud+" Su área es: "+área+ 
                " Y su volúmen de esfera sería: "+volúmen);
     
        
        
    
    }
    
    
}
