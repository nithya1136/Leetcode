

char * mergeAlternately(char * word1, char * word2){
  int len1 = strlen(word1), len2 = strlen(word2);
  int total_len = len1 + len2;
  char *s = (char *)malloc((total_len + 1) * sizeof(char));
  if (!s) return NULL;
  int c=1,i=0,j=0,k=0;
  while(word1[j] && word2[k]){
    if(c)
        s[i++]=word1[j++];
    else
        s[i++]=word2[k++];
    c=!c;
  }
  while(word1[j])
    s[i++]=word1[j++];
  while(word2[k])
    s[i++]=word2[k++];
  s[i]='\0';
  return s;
}