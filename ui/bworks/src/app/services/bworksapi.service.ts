import { Injectable } from '@angular/core';

import { HttpClient } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { Data } from '@angular/router';
import { HttpHeaders } from '@angular/common/http';
import { User, LoginRequest, Bicycle, Transaction, RegisterUser } from '../datamodels/bworksmodel';


@Injectable({
  providedIn: 'root'
})
export class BworksapiService {

  constructor(private http: HttpClient) { }

  login(data: LoginRequest): Observable<any> {

    const httpOptions = {
      headers: new HttpHeaders({
        'Content-Type':  'application/json'
      })
    };

    const url = "http://127.0.0.1:5000/login"
    return this.http.post<User>(url, data, httpOptions);
    
  }

  register(data: RegisterUser): Observable<any> {

    //const headers = new HttpHeaders().set('Content-Type','text/plain; charset=utf-8');

    const url = "http://127.0.0.1:5000/register"
    return this.http.post<User>(url, data );
  }

  getBicycles(): Observable<any> {

    const url = "http://127.0.0.1:5000/bicycle"
    return this.http.get<Bicycle[]>(url);
    
  }

  transaction(data: Transaction): Observable<any> {

    const httpOptions = {
      headers: new HttpHeaders({
        'Content-Type':  'application/json'
      })
    };

    const url = "http://127.0.0.1:5000/transaction"
    return this.http.post<User>(url, data, httpOptions);
    
  }
  
}


