import { Injectable } from '@angular/core';
import { Observable } from 'rxjs/Observable';
import 'rxjs/add/observable/of';
import 'rxjs/add/operator/delay';
import { CHARACTERS } from './mock-data';
@Injectable()


@Injectable({
  providedIn: 'root'
})
export class NflScoresService {

  constructor() { }

  getCharacters(): Observable<any[]>{
  	return Observable.of(CHARACTERS).delay(100);
  }

  getColumns(): string[] {
  	return ["Date of Contest","Home team","Away team","Home team scores","Away team scores"]};
}
