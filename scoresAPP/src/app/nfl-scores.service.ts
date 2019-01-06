import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { NFL_SCORES } from './nflScores-data';
import { HttpClient } from '@angular/common/http';
@Injectable()


@Injectable({
  providedIn: 'root'
})
export class NflScoresService {

  constructor(private httpClient: HttpClient) { }

  getCharacters(): Observable<any>{
    let nflScores = this.httpClient.get("/api/scores");
    console.log(nflScores);

  	return nflScores;
  }

  getColumns(): string[] {
  	return ["Date of Contest","Home team","Away team","Home team scores","Away team scores"]};
}
