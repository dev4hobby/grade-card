import _ from 'lodash'

export enum gradeCard {
  ID = 'ID',
  Name = 'name',
  Desc = 'desc',
  UserID = 'userID',
  TestID = 'testID',
  MyAnswers = 'myAnswers', // 내 정답과 TestID로 가져온 Question 비교
  Achievements = 'achievements', // 성취도
  ScoreReferences = 'scoreReferences', // 성적 추이
}

export interface IGradeCard {
  id: number
  name: string
  desc: string
  userID: number
  testID: number
  myAnswers: JSON
  achievements: JSON
  scoreReferences: JSON
}
