# USAGE: bash personal_email.sh -s=[SUBJECT] -b=[BODY] -a=[ATTACHMENT]
PERSONAL_EMAIL="marcograca89@gmail.com"
SUBJECT="Subject"
BODY="Body"

for i in "$@"; do
  case $i in
    -s=*|--subject=*)
      SUBJECT="${i#*=}"
      shift 
      ;;
    -b=*|--body=*)
      BODY="${i#*=}"
      shift
      ;;
    -a=*|--attachment=*)
      ATTACHMENT="${i#*=}"
      shift 
      ;;
    -*|--*)
      echo "Unknown option $i"
      exit 1
      ;;
    *)
      ;;
  esac
done


if [ -z "$ATTACHMENT" ]; then
    mail -s "$SUBJECT" "$PERSONAL_EMAIL" <<< "$BODY"
else
    mail -s "$SUBJECT" -a "$ATTACHMENT" "$PERSONAL_EMAIL" <<< "$BODY"
fi

