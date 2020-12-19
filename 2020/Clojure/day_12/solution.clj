(ns day_12.solution
  (:require [clojure.string :as str]
            [main :as main :refer [defoverload]]))

(def day "12")

(defn get-lines
  "Read in and parse inputs as seq of vectors."
  [file]
  (letfn [(parse [s]
            (let [[direction num] (re-seq #"[A-Z]|[0-9]+" s)]
              [direction (read-string num)]))]
    (->> file
         slurp
         str/split-lines
         (map parse))))

;(defn circuitous-escape
;  []
;  (letfn [(chiral-move [x y now-face direction step]
;            (case now-face
;              "N" (cond
;                    (= direction "L") [(- x step) y "W"]
;                    (= direction "R") [(+ x step) y "E"]
;                    :else [(+ x step) y "E"]
;                    )
;              "S" (if (= direction "L")
;                    [(+ x step) y "E"]
;                    [(- x step) y "W"])
;              "W" (if (= direction "L")
;                    [x (- y step) "S"]
;                    [x (+ y step) "N"])
;              "E" (if (= direction "L")
;                    [x (+ y step) "N"]
;                    [x (- y step) "S"])))
;          (directional-move [x y direction step]
;            (case direction
;              "N" [x (+ step y)]
;              "S" [x (- step y)]
;              "W" [(- x step) y]
;              "E" [(+ x step) y]))]
;    (loop [inputs inputs
;           x 0
;           y 0
;           now-face "E"]
;      (let [[direction step] (first inputs)]
;        (if #{"L" "R"}))))
;  )

(defn part1
  [_]
  nil)

(defn part2
  [_]
  nil)

(defoverload main/part1 day part1)
(defoverload main/part2 day part2)
