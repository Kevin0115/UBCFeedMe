import { Injectable } from '@angular/core';
import {Http} from "@angular/http";
import 'rxjs';

@Injectable()
export class PostsService {

  constructor(private http: Http) { }

  getAllPosts() {
    var posts = this.http.get('/api/posts').map(res => res.json());

    return posts;
  }

}
