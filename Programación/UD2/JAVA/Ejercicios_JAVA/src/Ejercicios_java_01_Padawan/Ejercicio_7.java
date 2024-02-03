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
 * Ejercicio_7: Escribe un programa que lea un valor correspondiente
 * a una distancia en millas marinas y escriba la distancia en metros 
 * Sabiendo que una milla marina equivale a 1.852 metros.
 * ***********************************************************************
 * 
 */

//Importamos el java.util.Scanner
import java.util.Scanner;
public class Ejercicio_7 {
    
     public static void main(String[] args){
     
        //Definimos las variables que vamos a usar
        double distancia_millas, distancia_metros;
        
        //Declaro el objeto lector el cual es un scanner
        Scanner lector = new Scanner(System.in);
        
        /**
         * Ahora muestro en pantalla el mensaje que dirá que se introduzca el 
         * valor para la distancia.
         */
        
        System.out.println("Introduzca la distancia deseada: ");
        
        //Introducimos el aparatado de entrada de la distancia en millas
        distancia_millas = lector.nextDouble();
        
        //Ahora realizamos las operaciones necesarias
        distancia_metros = (distancia_millas*1852);
        
        //Ahora mostraré en pantalla el mensaje que dará la solución.
         System.out.println("La distancia en metros de "+distancia_millas+
         " millas, es de: "+distancia_metros+" metros");
     
     
     }
}
