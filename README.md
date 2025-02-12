<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <title>테이블 스타일 적용</title>
</head>
<body>

  <!-- 첫 번째 테이블 -->
  <h2>일반 내용</h2>
  <table style="border-collapse: collapse; width: 100%;">
    <tr>
      <th style="border: 1px solid black; padding: 8px; text-align: left; font-family: '맑은 고딕', monospace; background-color: yellow;">
        주제
      </th>
      <th style="border: 1px solid black; padding: 8px; text-align: left; font-family: '맑은 고딕', monospace; background-color: yellow;">
        Part
      </th>
      <th style="border: 1px solid black; padding: 8px; text-align: left; font-family: '맑은 고딕', monospace; background-color: yellow;">
        URL
      </th>
    </tr>
    <tr>
      <td style="border: 1px solid black; padding: 8px;">구글클라우드, 유통 혁신 지원하는 AI 솔루션 대거 공개</td>
      <td style="border: 1px solid black; padding: 8px;">뉴스기사</td>
      <td style="border: 1px solid black; padding: 8px;"><a href="https://zdnet.co.kr/view/?no=20230116113210">링크</a></td>
    </tr>
    <tr>
      <td style="border: 1px solid black; padding: 8px;">BigQuery ML에서 분류 모델로 방문자 구매 예측하기</td>
      <td style="border: 1px solid black; padding: 8px;">실습</td>
      <td style="border: 1px solid black; padding: 8px;"><a href="https://www.cloudskillsboost.google/focuses/1794?locale=ko&parent=catalog">링크</a></td>
    </tr>
    <tr>
      <td style="border: 1px solid black; padding: 8px;">구글 클라우드가 정리하여 공개한 실세계 생성형 AI 활용사례</td>
      <td style="border: 1px solid black; padding: 8px;">파이토치 블로그</td>
      <td style="border: 1px solid black; padding: 8px;"><a href="https://discuss.pytorch.kr/t/google-cloud-ai-321-1-6-customer-agents/5897">링크</a></td>
    </tr>
  </table>

  <!-- 두 번째 테이블 -->
  <h2>마케팅 퍼포먼스 및 분석</h2>
  <h3> (참고자료: git - GPT답변폴더 - GPT o3 - 이커머스 AARRR에서 에이전트까지.pdf) </h3> 
  <table style="border-collapse: collapse; width: 100%;">
    <tr>
      <th style="border: 1px solid black; padding: 8px; text-align: left; font-family: '맑은 고딕', monospace; background-color: yellow;">
        주제
      </th>
      <th style="border: 1px solid black; padding: 8px; text-align: left; font-family: '맑은 고딕', monospace; background-color: yellow;">
        Part
      </th>
      <th style="border: 1px solid black; padding: 8px; text-align: left; font-family: '맑은 고딕', monospace; background-color: yellow;">
        URL
      </th>
    </tr>
    <tr>
      <td colspan="3" style="border: 1px solid black; padding: 8px; text-align: center; font-weight: bold; background-color: yellow;">
        마케팅 퍼포먼스를 개선하기 위한 GA4 BigQuery를 활용한 유입 경로별 전환율 분석
      </td>
    </tr>
    <tr>
      <td style="border: 1px solid black; padding: 8px;">퍼널 분석에 대하여 먼저 읽기</td>
      <td style="border: 1px solid black; padding: 8px;">구글검색 'funnel 분석'</td>
      <td style="border: 1px solid black; padding: 8px;"><a href="https://ssongblog.tistory.com/34">링크</a></td>
    </tr>
    <tr>
      <td style="border: 1px solid black; padding: 8px;">오늘의집 A/B 실험 플랫폼 구축기 <br> 오늘의집 A/B 실험 플랫폼 구축 과정과 그 속에서 해결한 고민들<br> 
(기술 블로그 임으로 추후에 다시 자세히 보세요. <br> 
채용공고도 있음. 경력직이 대다수임)</td>
      <td style="border: 1px solid black; padding: 8px;">블로그 (읽어만 보셔요)</td>
      <td style="border: 1px solid black; padding: 8px;">
        <a href="https://www.bucketplace.com/post/2021-10-29-%EC%98%A4%EB%8A%98%EC%9D%98%EC%A7%91-a-b-%EC%8B%A4%ED%97%98-%ED%94%8C%EB%9E%AB%ED%8F%BC-%EA%B5%AC%EC%B6%95%EA%B8%B0/">링크</a>
      </td>
    </tr>
    <tr>
      <td style="border: 1px solid black; padding: 8px;">A/B 테스트 계산기</td>
      <td style="border: 1px solid black; padding: 8px;"></td>
      <td style="border: 1px solid black; padding: 8px;"><a href="https://yozm.wishket.com/magazine/detail/1656/">링크</a></td>
    </tr>
    <tr>
      <td style="border: 1px solid black; padding: 8px;">A/B 테스트에 대하여 자세히 설명</td>
      <td style="border: 1px solid black; padding: 8px;"></td>
      <td style="border: 1px solid black; padding: 8px;"><a href="https://www.shopify.com/kr/blog/the-complete-guide-to-ab-testing">링크</a></td>
    </tr>
    <tr>
      <td style="border: 1px solid black; padding: 8px;">구글 빅쿼리_EDA 자세히 (이탈률/종료율 분석)</td>
      <td style="border: 1px solid black; padding: 8px;">블로그</td>
      <td style="border: 1px solid black; padding: 8px;">
        <a href="https://velog.io/@kjmn1105/BigQuery%EB%A1%9C-Google-Analytics-%EB%8D%B0%EC%9D%B4%ED%84%B0-%EB%B6%84%EC%84%9D%ED%95%98%EA%B8%B0-1-%ED%95%84%EC%82%AC">
          링크
        </a>
      </td>
    </tr>
    <tr>
      <td style="border: 1px solid black; padding: 8px;">구글 빅쿼리 & GA를 이용한 구매전환율 개선</td>
      <td style="border: 1px solid black; padding: 8px;">블로그</td>
      <td style="border: 1px solid black; padding: 8px;"><a href="https://datarian.io/blog/how-we-dramatically-improved-conversion-rates">링크</a></td>
    </tr>
  </table>

</body>
</html>
