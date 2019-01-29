import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { HttpClient } from '@angular/common/http';
@Injectable()


@Injectable({
  providedIn: 'root'
})
export class NflScoresService {

  constructor(private httpClient: HttpClient) { }

  getNFLScores(): Observable<any>{
    let nflScores = this.httpClient.get("/api/scores");
  	return nflScores;
  }

  getColumns(): string[] {
  	return ["Date of Contest","Home team","Away team","Home team scores","Away team scores"]};
}
