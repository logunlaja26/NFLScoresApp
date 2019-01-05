import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';
import { NFL_SCORES } from './nflScores-data';
@Injectable()


@Injectable({
  providedIn: 'root'
})
export class NflScoresService {

  constructor() { }

  getCharacters(): Observable<any[]>{
    console.log('nfl_scores', NFL_SCORES);
  	return of(NFL_SCORES);
  }

  getColumns(): string[] {
  	return ["Date of Contest","Home team","Away team","Home team scores","Away team scores"]};
}
