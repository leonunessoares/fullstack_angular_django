import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class PessoaService {
  private apiUrl = 'http://localhost:8000/api/pessoas/';
  private pesoUrl = 'http://localhost:8000/api/calcular_peso_ideal/';

  constructor(private http: HttpClient) { }

  getPessoas(): Observable<any> {
    return this.http.get(this.apiUrl, { headers: this.getHeaders() });
  }

  getPessoa(id: number): Observable<any> {
    return this.http.get(`${this.apiUrl}${id}/`, { headers: this.getHeaders() });
  }

  addPessoa(pessoa: any): Observable<any> {
    return this.http.post(this.apiUrl, pessoa, { headers: this.getHeaders() });
  }

  updatePessoa(id: number, pessoa: any): Observable<any> {
    return this.http.put(`${this.apiUrl}${id}/`, pessoa, { headers: this.getHeaders() });
  }

  deletePessoa(id: number): Observable<any> {
    return this.http.delete(`${this.apiUrl}${id}/`, { headers: this.getHeaders() });
  }

  calcularPesoIdeal(altura: number, sexo: string): Observable<any> {
    return this.http.post(this.pesoUrl, { altura, sexo }, { headers: this.getHeaders() });
  }

  private getHeaders(): HttpHeaders {
    return new HttpHeaders({
      'Content-Type': 'application/json',
      'Accept': 'application/json'
    });
  }
}
