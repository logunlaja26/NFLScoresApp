import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';
import { CHARACTERS } from './mock-data';
@Injectable()


@Injectable({
  providedIn: 'root'
})
export class NflScoresService {

  constructor() { }

  getCharacters(): Observable<any[]>{
  	return of(CHARACTERS);
  }

  getColumns(): string[] {
  	return ["Date of Contest","Home team","Away team","Home team scores","Away team scores"]};
}
